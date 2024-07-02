import time

import requests

cookies = {
    'thw': 'cn',
    'wk_cookie2': '15e6f73db290b0de9929a3e0899160fc',
    'wk_unb': 'UNQ1zQaTaBiP1Q%3D%3D',
    'useNativeIM': 'false',
    'wwUserTip': 'false',
    'havana_lgc_exp': '1716214296288',
    'hng': 'CN%7Czh-CN%7CCNY%7C156',
    '_uetvid': 'f4cbc2b0203611ef905a17d3910aa681',
    't': '452cc618ee8f36c0bf67ea89077a53ab',
    'xlly_s': '1',
    'mt': 'ci=0_0',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': 'b8062ca0c62f2fa4212857e1ce14109a_1719842599285',
    '_m_h5_tk_enc': 'a38638b9ba5f31a48fc5a0ab3551270e',
    '_tb_token_': '331b613f555e5',
    '_samesite_flag_': 'true',
    '3PcFlag': '1719833604474',
    'cookie2': '1fe6e7f9a20d72c2cf1356076032d44e',
    'sgcookie': 'E100ESSr%2Fm6Ojm7B2SzBrMAi3KQDwSpu3ewklL4OdIGYMjqMF%2FurEYuRmLTRMRG0zIz8lcqlJmewYEefobbs3HQxePp8HRYYkOmegHXT2ZvuXi8%3D',
    'unb': '3428168582',
    'uc1': 'cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie14=UoYfqCMNlGg6hA%3D%3D&pas=0&cookie21=VT5L2FSpccLuJBreK%2BBd',
    'uc3': 'lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3i41bUbk7AHYnj4%3D&id2=UNQ1zQaTaBiP1Q%3D%3D&nk2=F6k3HS2idIIgrtmJ9T9sDk5Tqk8%3D',
    'csg': '64aba370',
    'lgc': 't_1514765822286_0155',
    'cancelledSubSites': 'empty',
    'cookie17': 'UNQ1zQaTaBiP1Q%3D%3D',
    'dnk': 't_1514765822286_0155',
    'skt': 'e71f3dee803ce6e5',
    'existShop': 'MTcxOTgzMzY0NQ%3D%3D',
    'uc4': 'nk4=0%40FbMocxjfKIWTSz5lJZC%2B7AXCeBVpsEK49pyhibtm7w%3D%3D&id4=0%40UgP%2Bi90ljAAr5P6LYLhXkwQQcbrU',
    'tracknick': 't_1514765822286_0155',
    '_cc_': 'V32FPkk%2Fhw%3D%3D',
    '_l_g_': 'Ug%3D%3D',
    'sg': '528',
    '_nk_': 't_1514765822286_0155',
    'cookie1': 'B0SsG%2FL%2BpMAKvPt7X9TWXirNiQxhQe%2BqRNjXDORwjso%3D',
    'tfstk': 'fz3ttJbhtpvM6L-m5ftnimEyxFR3HVhwIAl5o-2GcvHKGJbD_Px4kxeK3Rqg5RbYkjHqnxh2_SwjhxemjHYo_fz4lLmvrUcwUwjhYAEbG9ObG7Q6WexH1fz4lpfhl3Y-_YLcv_pYcBUQMS_bllZfAJwUiGwjhRZCd7Fzl-MblBEQN7115ow_OkNqZVfTn1wAkme4pUleEL7F82FB38hOPwNqy5BgefwpFS0T6twS1JQflRrRX5GKsdQrtPu-e7DMRNH-GbobvqBBe-uKOVijTOdQyXnnqlnpCZenSJrr5zCX5XUTBugZC1QZFXhjqk3HNUzT5Ri07jfJIX3tIfuKissQWPmL2VUWzOwmxb3YMqJ2JYhjamZKkOIyd40-KTXueSj69BIV0lN33Qh7te1e2qVLEBjh0ir3TWek9BIV0lNU98AH-iS4xW5..',
    'isg': 'BPDwLbNnYnEzlz0NN9swu4ewwb5COdSD6I7hzepBvMsepZBPkkmkE0aT_a3FNYxb',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'thw=cn; wk_cookie2=15e6f73db290b0de9929a3e0899160fc; wk_unb=UNQ1zQaTaBiP1Q%3D%3D; useNativeIM=false; wwUserTip=false; havana_lgc_exp=1716214296288; hng=CN%7Czh-CN%7CCNY%7C156; _uetvid=f4cbc2b0203611ef905a17d3910aa681; t=452cc618ee8f36c0bf67ea89077a53ab; xlly_s=1; mt=ci=0_0; mtop_partitioned_detect=1; _m_h5_tk=b8062ca0c62f2fa4212857e1ce14109a_1719842599285; _m_h5_tk_enc=a38638b9ba5f31a48fc5a0ab3551270e; _tb_token_=331b613f555e5; _samesite_flag_=true; 3PcFlag=1719833604474; cookie2=1fe6e7f9a20d72c2cf1356076032d44e; sgcookie=E100ESSr%2Fm6Ojm7B2SzBrMAi3KQDwSpu3ewklL4OdIGYMjqMF%2FurEYuRmLTRMRG0zIz8lcqlJmewYEefobbs3HQxePp8HRYYkOmegHXT2ZvuXi8%3D; unb=3428168582; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&cookie14=UoYfqCMNlGg6hA%3D%3D&pas=0&cookie21=VT5L2FSpccLuJBreK%2BBd; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3i41bUbk7AHYnj4%3D&id2=UNQ1zQaTaBiP1Q%3D%3D&nk2=F6k3HS2idIIgrtmJ9T9sDk5Tqk8%3D; csg=64aba370; lgc=t_1514765822286_0155; cancelledSubSites=empty; cookie17=UNQ1zQaTaBiP1Q%3D%3D; dnk=t_1514765822286_0155; skt=e71f3dee803ce6e5; existShop=MTcxOTgzMzY0NQ%3D%3D; uc4=nk4=0%40FbMocxjfKIWTSz5lJZC%2B7AXCeBVpsEK49pyhibtm7w%3D%3D&id4=0%40UgP%2Bi90ljAAr5P6LYLhXkwQQcbrU; tracknick=t_1514765822286_0155; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=528; _nk_=t_1514765822286_0155; cookie1=B0SsG%2FL%2BpMAKvPt7X9TWXirNiQxhQe%2BqRNjXDORwjso%3D; tfstk=fz3ttJbhtpvM6L-m5ftnimEyxFR3HVhwIAl5o-2GcvHKGJbD_Px4kxeK3Rqg5RbYkjHqnxh2_SwjhxemjHYo_fz4lLmvrUcwUwjhYAEbG9ObG7Q6WexH1fz4lpfhl3Y-_YLcv_pYcBUQMS_bllZfAJwUiGwjhRZCd7Fzl-MblBEQN7115ow_OkNqZVfTn1wAkme4pUleEL7F82FB38hOPwNqy5BgefwpFS0T6twS1JQflRrRX5GKsdQrtPu-e7DMRNH-GbobvqBBe-uKOVijTOdQyXnnqlnpCZenSJrr5zCX5XUTBugZC1QZFXhjqk3HNUzT5Ri07jfJIX3tIfuKissQWPmL2VUWzOwmxb3YMqJ2JYhjamZKkOIyd40-KTXueSj69BIV0lN33Qh7te1e2qVLEBjh0ir3TWek9BIV0lNU98AH-iS4xW5..; isg=BPDwLbNnYnEzlz0NN9swu4ewwb5COdSD6I7hzepBvMsepZBPkkmkE0aT_a3FNYxb',
    'referer': 'https://s.taobao.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.7.2',
    'appKey': '12574478',
    't': int(time.time() * 1000),
    'sign': '91ad00505e625614dc9bac48131f220c',
    'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
    'v': '2.0',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp1',
    'data': '{"appId":"34385","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc\\",\\"page\\":\\"6\\",\\"n\\":48,\\"q\\":\\"%E5%A5%B3%E8%A3%85\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"categoryp\\":\\"\\"}"}',
}

print()
response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)