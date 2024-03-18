# coding: utf-8

import flet as ft
import openai
import pprint

def main(page: ft.Page):

    def request2gpt(e):
        
        if question.value:
            msg = "{}さんこんにちは".format(question.value)

        ans.value = msg
        ans.update()

    page.title = "GPU Gadget" # App Title

    question = ft.TextField(label="GPTに聞きたいこと")
    
    ans = ft.TextField(label="GPTからの返答内容", disabled=True)

    # judge = ft.ElevatedButton("判定", icon="gavel")
    judge = ft.ElevatedButton("GPTに質問する", icon="gavel", on_click=request2gpt)

    page.add(question, ans, judge)  # 5つのコントロールを配置
    

ft.app(target=main)


# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER, port=8890)