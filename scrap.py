from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

class Scrap:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Adicione essa linha para executar o Chrome em modo headless
        self.driver = webdriver.Chrome(options=self.options)

    from bs4 import BeautifulSoup

    
    def get(self):
        driver = self.driver
        driver.get('https://estudanteead.com/oficial/lista_cursos.php')

        element = driver.find_element("css selector", 'body')  # Filtrar somente
        html_content = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encontra todos os elementos <div class="modal-content">
        modal_content_divs = soup.find_all('div', class_='modal-content')

        data = {
            'Curso': [],
            'Aulas': [],
            'Descrição': []
        }

        for modal_content_div in modal_content_divs:
            cursos = modal_content_div.find_all('div')[2]
            aulas = modal_content_div.find_all('span')[-1]
            desc = modal_content_div.find_all('div')[3]

            curso_text = cursos.text.strip()
            aulas_text = aulas.text.strip()
            desc_text = desc.text.strip()

            data['Curso'].append(curso_text)
            data['Aulas'].append(aulas_text)
            data['Descrição'].append(desc_text)

        df = pd.DataFrame(data)
        df.to_excel('arquivo.xlsx', index=False)
        print(df)

        
        return
