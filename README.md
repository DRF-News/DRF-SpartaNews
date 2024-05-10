# 📋 스파르타 뉴스 심화과제 / DRF-SpartaNews

<br/>

DRF-SpartaNews는 DRF를 이용해서 만든 주요 뉴스와 정보를 제공하는 사이트입니다.

<br/>
<br/>

## 📅 프로젝트 일정

<br/>

개발 기간 : 2024년 05월 06일(월) - 2024년 05월 10일(금)

<br/>
<br/>

## 🧑‍💻 팀 멤버 구성 

<br/>

- **강슬범(Search)** [@kngslbm] (https://github.com/kngslbm)
- **이성준(User)** [@zyersnw] (https://github.com/zyersnw)
- **이정우(Post)** [@JWTONE] (https://github.com/JWTONE)
- **이진원(Comment)** [@leejinwon012] (https://github.com/leejinwon012)
- **현효민(Accounts, Open AI)** [@HyunHyoMin] (https://github.com/HyunHyoMin)

<br/>
<br/>


## 🛠️ 주요 기능

<br/>

**현효민(Accounts)**
- **[회원가입, 로그인, 로그아웃](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Accounts/views.py#L13)**
- **[회원정보 변경](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Accounts/views.py#L21)**
- **[회원탈퇴](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Accounts/views.py#L32)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Accounts/urls.py#L9)

 <br/>

- **[OpenAI 요약](https://github.com/DRF-News/DRF-SpartaNews/blob/main/chatgpt/views.py#L9)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/chatgpt/urls.py#L3)   

<br/>

**이성준(User)**
- **[좋아요 누른 게시글 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/User/views.py#L18)**
- **[즐겨찾기 한 게시글 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/User/views.py#L29)**
- **[유저 상세 페이지 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/User/views.py#L11)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/User/urls.py#L5)

<br/>

**이정우(Post)**
- **[게시글 목록 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/views.py#L11)**
- **[게시글 자세히 보기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/views.py#L25)**
- **[게시글 작성, 수정, 삭제하기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/views.py#L16)**
- **[게시글 좋아요](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/views.py#L43)**
- **[게시글 북마크](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/views.py#L62)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Post/urls.py#L10)

<br/>

**이진원(Comment)**
- **[댓글 작성, 수정, 삭제하기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Comment/views.py#L11)**
- **[댓글 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Comment/views.py#L72)**
- **[대댓글 보여주기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Comment/views.py#L100)**
- **[대댓글 작성, 수정, 삭제하기](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Comment/views.py#L81)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Comment/urls.py#L4)

<br/>

**강슬범(Search)**
- **[검색](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Search/views.py#L9)**
  - [API 엔드포인트](https://github.com/DRF-News/DRF-SpartaNews/blob/main/Search/urls.py#L5)

<br/>
<br/>



## 💻 사용 기술 및 개발 환경

- **Django** : 웹 애플리케이션 개발을 위한 파이썬 기반 프레임워크입니다.
- **Django REST Framework (DRF)**: Django를 사용하여 RESTful API를 구축하는 데 도움을 주는 도구입니다.
- **SQLite**: 경량의 관계형 데이터베이스 관리 시스템으로, Django의 기본 데이터베이스로 사용되었습니다.
- **Git 및 GitHub**: 버전 관리 및 협업을 위한 도구들입니다.


<br/>
<br/>



## 🚀 기능 상세

<br/>

### **회원 기능 및 Open AI (현효민)**
- **회원가입** : 사용자는 회원가입 양식을 작성하여 새 계정을 생성할 수 있습니다.
- **로그인, 로그아웃** : 이미 가입한 사용자는 등록된 username과 비밀번호를 사용하여 로그인, 로그아웃을 할 수 있습니다.
- **회원정보 변경** : 사용자는 회원정보를 변경할 수 있습니다.
- **회원 비밀번호 변경** : 사용자는 비밀번호와 새 비밀번호를 입력하여 비밀번호를 변경할 수 있습니다.
- **회원탈퇴** : 사용자는 계정을 삭제하여 회원탈퇴할 수 있습니다. 탈퇴 시 사용자의 모든 정보가 삭제됩니다.
- **토큰 재발급** : 인증 토큰이 만료된 경우 사용자는 새로운 토큰을 요청하여 인증을 유지할 수 있습니다.
- **Open AI** : 자연어 처리 및 인공지능 기술을 통한 텍스트 생성 및 분석 서비스를 제공합니다.
- **OPENAI_API_KEY는 config.py에 OPENAI_API_KEY로 넣어놨습니다. 개인 키를 사용하시면 됩니다**

### **사용자 기능 (이성준)**
- **찜 목록 보여주기** : 사용자는 관심 있는 게시글을 찜 목록에 추가하여 나중에 쉽게 찾아볼 수 있습니다.
- **찜 댓글 목록 보여주기** : 사용자가 찜한 게시글에 작성된 댓글 목록을 볼 수 있습니다.
- **북마크 목록 보여주기** : 사용자가 북마크한 게시글 목록을 보여줍니다.

### **게시글 기능 (이정우)**
- **게시글 목록 보여주기** : 모든 사용자는 게시판에서 작성된 게시글을 볼 수 있습니다.
- **게시글 자세히 보기** : 사용자는 게시글을 클릭하여 자세한 내용을 확인할 수 있습니다.
- **게시글 작성, 수정, 삭제하기** : 사용자는 게시글을 작성하고, 수정하고, 삭제할 수 있습니다.
- **게시글 좋아요** : 사용자는 게시글에 좋아요를 표시할 수 있습니다.
- **게시글 북마크** : 사용자는 게시글을 북마크하여 나중에 쉽게 찾아볼 수 있습니다.

### **댓글 기능 (이진원)**
- **댓글 작성, 수정, 삭제하기** : 사용자는 게시글에 댓글을 작성하고, 수정하고, 삭제할 수 있습니다.
- **댓글 보여주기** : 게시글에 작성된 댓글 목록을 볼 수 있습니다.
- **대댓글 보여주기** : 댓글에 작성된 대댓글 목록을 볼 수 있습니다.
- **대댓글 작성, 수정, 삭제하기** : 사용자는 댓글에 대댓글을 작성하고, 수정하고, 삭제할 수 있습니다.

### **검색 기능 (강슬범)**
- **검색** : 사용자는 특정 키워드를 입력하여 게시글 및 댓글을 검색할 수 있습니다.

<br/>
<br/>


## 🗂️ 와이어프레임 및 ERD

<br/>

![와이어프레임](https://github.com/DRF-News/DRF-SpartaNews/assets/78424970/6de8e3b3-9718-43ae-82f2-2fec51d3e683)

![ERD](https://github.com/DRF-News/DRF-SpartaNews/assets/78424970/be65a655-0cec-48a4-a834-a318088c1cef)


<br/>
<br/>

## 📊 POSTMAN 구성

![postman 구성](https://github.com/DRF-News/DRF-SpartaNews/assets/78424970/03146551-8a27-406d-8dc9-6555e7c8d19d)








