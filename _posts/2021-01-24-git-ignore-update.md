---
layout: post
title: "gitignore 변경 사항 remote repo에 적용하기"
category: Sihan

tag:
  - Github
  - git
  - add
  - ignore
  - gitignore
comments: true
---

테크 블로그를 목표 시작한 블로그가 1년 넘게 IT 도서 서평 블로그가 되었습니다. 초심을 찾고자 오랜만에 `git`, `Github`를 주제로 돌아왔습니다. 오늘 내용은 `Github`에만 적용 되는 내용은 아니고 `bitbucket`, `gitlab`에서도 동일하게 적용되는 내용이지만 제 주 서식처가 `github`인 관계로 `github`가 메인입니다.

`git`을 이용해 프로젝트를 진행하다 보면 굳이 버전관리가 필요 없거나 `remote repo`인 `Github`등에 올리면 안되거나, 필요가 없는 것들이 존재합니다. `git`에 좀 익숙하신 분들이라면 이런 파일이나 디렉토리를 관리하기 위해서 `.gitignore`을 대충이라도 써보셨거나 쓸 계획을 가지고 계실 것입니다. `gitignore`에 대한 자세한 내용은 조만간 다른 글로 돌아오겠습니다.

시작 단계에서는 필요를 못 느꼈던 파일이나 디렉토리가 프로젝트를 진행하다 보면 생기기 마련입니다. 그런데 어느새 `git add .`나 ide에서 단축키를 이용해서 `add`를 하다보면 올려선 안 될 것들이 이미 `github`에서 자리를 떡하니 잡고 올라가 있습니다. 그래서 급하게 `gitignore` 파일을 열어서 급하게 추가해 보지만 이미 올라간 파일은 `indexing`이 되어서 내려오지 않고 있습니다. 오늘 이 문제의 해결 방법입니다.

```git
git add "<file | directoty>"
```

를 하게 되면 인덱싱이 되어 그 때 부터 버전관리를 하게 됩니다. `gitignore`에 추가를 하게 되도 인덱싱 된 캐시가 있기 때문에 추가로 생성된 파일이나 경로가 아니라면 기존의 것들은 계속해서 버전 관리가 되고 `remote repo`에 잔류하게 되는 것 입니다.

해결 방법은 의외로 굉장히 간단합니다. 캐싱이 문제라면 캐시를 정리하면 되겠죠?

```git
git rm --cached "<file | *.file extension>"
gir rm -r --cached <directoty>

ex)
git rm --cached *.log
git rm -r --cached .idea
```

로 캐시를 정리 해주면 문제는 의외로 굉장히 간단하게 해결 됩니다. 이후 `commit` 후 `push`를 하면 `remote repo`에 올라 가 있던 파일이나 디렉토리가 사라진 것을 확인 할 수 있습니다.

디렉토리를 제외하는 명령에는 `-r`이 있는 것을 볼 수 있습니다. 보통의 디렉토리들이 계층 구조를 가지고 있어서 재귀적으로 명령을 수행 해야해서 `-r`없이 실행하면 `fatal: not removing '<directory>' recursively without -r `같은 에러 메세지를 만날 수 있습니다. 그래서 디렉토리를 제외하는 경우에는 `-r`을 붙여주는 습관을 들이는 것도 나쁘지 않습니다.
