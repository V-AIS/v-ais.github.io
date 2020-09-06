---
layout: post
title:  "Pandoc으로 Markdown Github-style 렌더링하기"
category: Sihan
tag:
- Github
- markdown
- pandoc
---

`Pandoc`이라는 `Haskell`로 작성 된 `converter`로 `markdown`, `mediawiki`, `textile`, `HTML`, `docx(ms word)`, `epub`, `PDF` 등으로 변화이 가능한 유틸리입니다.  

 # 설치

 [다운로드](https://github.com/jgm/pandoc/releases)에서 스크롤을 내리시면 `OS`별로 설치 파일을 받을 수 있습니다. `OS` 버전에 맞는 걸로 설치 해주세요. 

 # 주요 옵션
 
 |        옵션                 | 설명        |
 |-----------------------------|-------------|
 |-o FILENAME, --output=FILENAME| 저장할 파일명|
 |-f FORMAT, --from=FORMAT      | 소스 포맷   |
 |-t FORMAT,--to=FORMAT	        |저장할 포맷	|
 |--toc                         |목차 생성	|
 |-S, --smart	|pandoc 이 소스 포맷을 판단해서 처리	|
 |-s, --standalone	|파일이 아닌 STDIN 에서 입력 수행	|
 |-c URL, --css=URL |변환시 사용할 CSS 의 URL	|
 |-H FILENAME, --include-in-header=FILENAME 	|FILENAME 을 HEADER 로 사용	|
 |-A FILENAME, --include-after-body=FILENAME	|FILENAME 을 footer 로 사용	|

> -o FILENAME은 필수 옵션입니다.


# Github Style로 변환하기

[GitHub Sytle](https://gist.github.com/dashed/6714393)에 들어가셔서 `CSS`파일을 다운로드 받아주세요. 이 포스팅의 가장 핵심인 파일입니다. 여기서 받은 파일을 `--css` 옵션으로 줘서 `Github-Style`로 만들수 있습니다.

```
pandoc test1.md -f markdown -t html -s --css=github-pandoc.css -o test1.html
```
위와 같이 `Markdown`파일이 있는 위치에 `css`파일도 두고 변환을 시켜주시면 됩니다. `PDF`로 바로 저장도 되지만 `LaTeX` 패키지가 필요해서 `LaTeX`유저가 아니시면 `HTML`로 변환 하시고 `PDF` 인쇄 옵션을 통해서 저장하셔도 괜찮습니다.

주의 하실 점은 `CSS`로 `HTML`을 꾸며서 만드는 것이기 떄문에 `CSS`파일의 위치 참조가 깨지면 다시 평문 형태로 돌아가기 때문에 추출한 파일을 이동하실 때에는 `CSS`파일과 같이 움직여 주세요.