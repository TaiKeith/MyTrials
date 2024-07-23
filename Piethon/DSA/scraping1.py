import requests, pandas as pd
from bs4 import BeautifulSoup

def get_clinic_name(clinic_id):
    url = f"https://{clinic_id}.portal.athenahealth.com/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    #soup.title.text.strip()
    clinic_name = soup.find_all("h1")[-1].text.strip()
    return clinic_name

start = 12690
end = 12710

m_list = []

for clinic_id in range(start, end + 1):
    data_dict = {}
    data_dict["clinic_id"] = clinic_id
    data_dict["clinic_name"] = get_clinic_name(clinic_id)
    m_list.append(data_dict)
    print(clinic_id)

df = pd.DataFrame(m_list)
df.to_csv("Clinic_Data.csv", index=False)
