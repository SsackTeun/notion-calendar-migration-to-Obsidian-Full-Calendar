## notion 에서 내보내기
## 1. notion 에서 캘린더파일을 제일 상위위치로 옮김

## 2. 우측 상단에 ... 에서 내보내기
- 내보내기 형식 : HTML 
- 데이터베이스 포함 : 현재 보기
- 하위 페이지 포함 : ON
- 하위 페이지용 폴더 생성 : OFF
- 댓글 내보내기 : OFF

## 새 Obsidian Valut 생성 후 Import
- 커뮤니티 플러그인 : Importer 설치
- NOTION.ZIP 으로 IMPORT
- 새 Obsidian Value 에서 .md 파일을 폴더포함하여 복사

## MD 파일중 아래 형식인 파일은 파일명을 calendar.md 로 고친후, 현재 디렉토리에 위치할 것
| 이름                 | 날짜                         | 태그  |
| ------------------ | -------------------------- | --- |
| [[캘린더 마이그레이션 테스트]] | 2024년 2월 26일               |     |
| [[teasdf]]         | 2024년 3월 5일                |     |
| [[test]]           | 2024년 3월 13일               |     |
| [[qewr]]           | 2024년 3월 21일               |     |
| [[휴가 2]]           | 2024년 2월 27일               |     |
| [[휴가]]             | 2024년 2월 26일 → 2024년 3월 2일 |     |

## 나머지 파일
- 이 프로그램의 경로인 source 에 붙여넣기

## 1_extract md file & move to workspace : 
- 실행시 폴더 포함하여, 내부에 있는 .md 파일을 전부 /workspace/input 으로 복사

## 2_ modify calendar property :
- 실행시 input 폴더 내부에 있는 .md 파일의 property 구조를 수정

## 3_(option) change title in property :
- output 폴더에서 .md 파일의 title : 에 있는 단어를 검색하여, 일괄로 공통 단어로 변경할 수 있음
- ex) title : 휴가, title : 휴가2 , title : 휴가 asdfqwe 이런 세가지 파일이 있다면,
- ex) title : 휴가, title : 휴가, title : 휴가 이런식으로 변경가능

## 4_(option) add date format to file name :
- 3과 기능은 동일하나, 파일명을 title + 일자로 변경 기능을 추가로 사용
- 파일명 : 
1. 휴가_2024-02-26_to_2024-03-02.md (기간인 경우)
2. 휴가_2024-02-27 (하루인 경우)




