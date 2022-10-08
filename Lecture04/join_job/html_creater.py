from cgitb import html
from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data

def create(device = 1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml += '</hml>'


def new_create(data, device = 1):
    t, p, w = data
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '</hml>'

    with open('new_index.xml', 'w') as page:
        page.write(xml)

    return data
