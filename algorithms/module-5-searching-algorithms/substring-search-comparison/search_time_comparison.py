from boyer_moore import boyer_moore as bm
from knuth_morris_pratt import knuth_morris_pratt as kmp
from rabin_karp import rabin_karp as rk
import requests
import timeit


def download_article(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)


url1 = (
    "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
)
url2 = (
    "https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"
)
article1 = download_article(url1)
article2 = download_article(url2)

algorithms = [bm, kmp, rk]

pattern_exist_article_1 = "Експоненціальний пошук використовується з"
pattern_not_exist_article_1 = (
    "Визначаються усі предмети, які належать до контрольної гілки"
)
pattern_exist_article_2 = "серії експериментів: кількість агентів 262144"
pattern_not_exist_article_2 = "кількість предметів 1048579999999"

print("Article 1:")
for algorithm in algorithms:
    print(
        f"{algorithm.__name__} (existing pattern): {measure_time(algorithm, article1, pattern_exist_article_1)} seconds"
    )
    print(
        f"{algorithm.__name__} (non existing pattern): {measure_time(algorithm, article1, pattern_not_exist_article_1)} seconds"
    )

print("\nArticle 2:")
for algorithm in algorithms:
    print(
        f"{algorithm.__name__} (existing pattern): {measure_time(algorithm, article2, pattern_exist_article_2)} seconds"
    )
    print(
        f"{algorithm.__name__} (non existing pattern): {measure_time(algorithm, article2, pattern_not_exist_article_2)} seconds"
    )

"""
Article 1:
boyer_moore (existing pattern): 0.010651125005097128 seconds
boyer_moore (non existing pattern): 0.009865041996818036 seconds
knuth_morris_pratt (existing pattern): 0.04247583300457336 seconds
knuth_morris_pratt (non existing pattern): 0.06941008300054818 seconds
rabin_karp (existing pattern): 0.09123408400046173 seconds
rabin_karp (non existing pattern): 0.15594120799505617 seconds

Article 2:
boyer_moore (existing pattern): 0.007470167009159923 seconds
boyer_moore (non existing pattern): 0.011977834001299925 seconds
knuth_morris_pratt (existing pattern): 0.069352374994196 seconds
knuth_morris_pratt (non existing pattern): 0.10505145900242496 seconds
rabin_karp (existing pattern): 0.1437887500069337 seconds
rabin_karp (non existing pattern): 0.2191590830043424 seconds

Results: boyer moore is the most fastest string seatch algorithm for existing and not existing pattern in a text!
"""
