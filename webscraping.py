import requests
from bs4 import BeautifulSoup
from mtranslate  import translate
# Veriyi almak için istek yap
url = 'https://forum.donanimarsivi.com/konu/sata-ssd-oenerisi-1tb.927887/'
response = requests.get(url)

# Yanıtı denetle ve hata ayıklama
if response.status_code == 200:
    # BeautifulSoup kullanarak HTML içeriğini ayrıştır
    soup = BeautifulSoup(response.text, 'html.parser')

    # Başlık al
    header = soup.find('h1', class_='p-title-value')
    if header:
        print("Başlık:", header.text.strip())

    # Alıntıları al
    contents = soup.find_all('article', class_='message--post')

    for content in contents:
        bb_wrapper = content.find('div', class_='bbWrapper')
        if bb_wrapper:
                # blockquote içeriği hariç tut
            for blockquote in bb_wrapper.find_all('blockquote'):
                blockquote.decompose()
            icerik = translate(bb_wrapper.get_text(strip=True),"eng")
            print("İçerik:", icerik)
else:
    print("Sayfa yüklenirken bir hata oluştu. Hata kodu:", response.status_code)