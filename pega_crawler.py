import os, csv, platform, argparse
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver

def main(args):
    # To do 
    # make csv file checker

    # Check Platform 
    if platform.system() == 'Windows':
        print('Detected OS : Windows')
        executable = './webdriver/chromedriver.exe'
    elif platform.system() == 'Linux':
        print('Detected OS : Linux')
        executable = './webdriver/chromedriver_linux'
    elif platform.system() == 'Darwin':
        print('Detected OS : Mac')
        executable = './webdriver/chromedriver_mac'

    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("lang=ko_KR") # 한국어!

    print("Pega's Post Crawling Start ! ")
    mode="headless"
    if mode == "headless":
        options.add_argument(mode)
    driver = webdriver.Chrome(executable, options=options)
    driver.implicitly_wait(1.5)

    category = f"{args.category}"
    tag = f"{args.tag}"
    dst = './_posts'
    os.makedirs(dst, exist_ok=True)
    root = "https://jehyunlee.github.io"
    main_page = f"https://jehyunlee.github.io/categories/{category}/{tag}/"
    driver.get(main_page)

    last_page = driver.find_element_by_xpath('//*[@id="page-nav"]/span[1]').text.split(' ')[-1]
    print(f"Number of pages: {last_page}")

    num_fieldnames = None

    try:
        csv_file_read = open('crawler_checker_pega.csv', mode='r')
        reader = csv.DictReader(csv_file_read)
        num_fieldnames = reader.fieldnames
        print("Checker file is already exist!")
    except:
        print("Checker file is  Not exist !")

    fieldnames = ['date', 'title', 'link']    
    csv_file_write = open('crawler_checker_pega.csv', mode='a')
    writer = csv.DictWriter(csv_file_write, fieldnames=fieldnames)
    
    title_in_csv = []

    if num_fieldnames:
        for row in reader:
            title_in_csv.append(row["title"])
    else:
        writer.writeheader()

    dates = []
    titles = []
    links = []
    excerpts = []
    thumbnails = []

    for page_num in tqdm(range(int(last_page), 0, -1)):
        if page_num != 1:
            driver.get(f"{main_page}/page/{page_num}/")
        else:
            driver.get(f"{main_page}")
        
        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        #article article-summary
        for i in soup.find_all(class_="article article-summary"):
            date = i.find(class_="date").text
            dates.append(date)
            
            title_herf = i.find(class_="article-title")
            title = title_herf.contents[1].text
            titles.append(title)
            
            if title in title_in_csv: continue

            print(f"New Post ! ({title})")
            link = root+title_herf.contents[1].get("href")
            links.append(link)
            
            excerpt = i.find(class_="article-excerpt").text
            excerpts.append(excerpt)
            
            thumbnail = root+i.find(class_="thumbnail-image").get("style")[:-1].split("(")[1]
            thumbnails.append(thumbnail)
            
            writer.writerow({'date': date, 'title': title, 'link': link})

            filename = os.path.join(dst, f"{date}-{link.split('/')[-2]}.md")

            full_text = f'---\nlayout: post\ntitle: {title_herf.contents[1].text}\ncategory: Pega\ntag:\n- Data Science\n---\n\n\n\n\n[![image]({thumbnail})]({link})'
            with open(f"{filename}", "w") as f:
                f.write(full_text)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", default='Python', type=str, help="Main Category")
    parser.add_argument("--tag", default='Data-Science', type=str, help="Tag")
    args = parser.parse_args()

    main(args)
