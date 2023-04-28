import io
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('agg')


def visualize_type(types_set):
    plot = plt
    types_money = {}
    types_companies = {}
    ttl_cost = 0
    for type_name, content in types_set.items():
        for item in content:
            types_money[type_name] = types_money.get(type_name, 0) + item[2][0]
            types_companies.setdefault(type_name, []).append(item[0])
            ttl_cost += item[2][0]
    percent_array = [round(float(value), 3) for value in types_money.values()]
    labels = [elem for elem in types_money.keys()]
    labels_cont = [str(key) + ': ' + ', '.join(value) for key, value in types_companies.items()]

    px = 1 / plt.rcParams['figure.dpi']
    fig = plt.figure(figsize=(1080 * px, 900 * px), facecolor='white')

    plot.pie(percent_array, labels=percent_array, shadow=True, autopct='%1.1f%%')
    plot.legend(labels)
    plot.title('Типы: ' + '\n' + '\n'.join(labels_cont) + '\n' + 'Общая сумма: ' + str(round(ttl_cost, 3)) + ' ₽')
    buf = io.BytesIO()
    plt.savefig(buf, dpi=300)
    buf.seek(0)
    im = Image.open(buf)
    plt.clf()
    return im


def visualize_industries(industries_set):
    plot = plt
    industries = {}
    ttl_cost = 0
    for company, content in industries_set.items():
        for element in content:
            industries[company] = industries.get(company, 0) + element[2][0]
            ttl_cost += element[2][0]
    percent_array = [round(float(value), 3) for value in industries.values()]
    labels = [elem for elem in industries.keys()]
    labels_cont = [str(key) + ': ' + str(round(value, 3)) for key, value in industries.items()]
    plot.pie(percent_array, labels=percent_array, shadow=True, autopct='%1.1f%%')
    plot.legend(labels)
    plot.title('Отрасли: ' + '\n' + '\n'.join(labels_cont) + '\n' + 'Общая сумма: ' + str(round(ttl_cost, 3)) + ' ₽')
    buf = io.BytesIO()
    plt.savefig(buf, dpi=300)
    buf.seek(0)
    im = Image.open(buf)
    plt.clf()
    return im


def visualize_companies(industries_set):
    plot = plt
    industries = {}
    ttl_cost = 0
    for company, content in industries_set.items():
        for element in content:
            industries[company] = industries.get(company, 0) + element[2][0]
            ttl_cost += element[2][0]
    percent_array = [round(float(value), 3) for value in industries.values()]
    labels = [elem for elem in industries.keys()]
    labels_cont = [str(key) + ': ' + str(round(value, 3)) for key, value in industries.items()]
    plot.pie(percent_array, labels=percent_array, shadow=True, autopct='%1.1f%%')
    plot.legend(labels)
    plot.title('Компании: ' + '\n' + '\n'.join(labels_cont) + '\n' + 'Общая сумма: ' + str(round(ttl_cost, 3)) + ' ₽')
    buf = io.BytesIO()
    plt.savefig(buf, dpi=300)
    buf.seek(0)
    im = Image.open(buf)
    plt.clf()
    return im


def visualize_currencies(currencies_set):
    plot = plt
    industries = {}
    ttl_cost = 0
    for company, content in currencies_set.items():
        for element in content:
            industries[element[1][1]] = industries.get(element[1][1], 0) + element[2][0]
            ttl_cost += element[2][0]
    percent_array = [round(float(value), 3) for value in industries.values()]
    labels = [elem for elem in industries.keys()]
    labels_cont = [str(key) for key, value in industries.items()]
    plot.pie(percent_array, labels=labels, shadow=True, autopct='%1.1f%%')
    plot.legend(labels)
    plot.title('Общая сумма: ' + str(round(ttl_cost, 3)) + ' ₽')
    buf = io.BytesIO()
    plt.savefig(buf, dpi=300)
    buf.seek(0)
    im = Image.open(buf)
    plt.clf()
    return im
