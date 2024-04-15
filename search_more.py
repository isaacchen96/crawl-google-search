from google_search import *
import os


def time_pass(start):
    t_pass = time.time() - start
    m_pass, s_pass = divmod(t_pass, 60)
    h_pass, m_pass = divmod(m_pass, 60)
    print('Time using: {:<2d} hour {:<3d} min {:<4.3f} sec\n'.format(int(h_pass), int(m_pass), int(s_pass)))

start = time.time()
crawler = crawler()
with open('search_list.txt', 'r+', encoding='UTF-8') as f:
    for query in  f.readlines():
        time.sleep(uniform(1, 5))
        crawler.write_results(query=query)
        time_pass(start)

