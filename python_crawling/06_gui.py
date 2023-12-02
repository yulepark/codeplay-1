import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def get_youtube_titles(query):
    # YouTube 검색 결과 페이지 HTML 가져오기
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    html = response.text

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 상위 5개의 영상 제목 가져오기
    video_titles = soup.select('.yt-lockup-title a[title]')
    titles = [title.get('title') for title in video_titles[:5]]

    return titles

def show_results():
    query = entry.get()

    # YouTube 검색 결과에서 상위 5개의 영상 제목 가져오기
    search_results = get_youtube_titles(query)

    # 검색 결과 표시 창 열기
    result_window = tk.Toplevel(root)
    result_window.title("YouTube 검색 결과")

    # 검색 결과 제목을 Label로 표시
    for idx, title in enumerate(search_results, 1):
        label = tk.Label(result_window, text=f"{idx}. {title}")
        label.pack(pady=5)

# GUI 설정
root = tk.Tk()
root.title("YouTube 검색")

# 검색어 입력 창
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# 검색 버튼
search_button = tk.Button(root, text="검색", command=show_results)
search_button.pack()

# GUI 실행
root.mainloop()
