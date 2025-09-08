from  lxml import html

def get_xp_data(file):
     page = ''
     with open(file, 'r', encoding='utf-8') as f:
          page = f.read()

     el = html.fromstring(page)

     item = {}
     k5 = 'Event Type'
     try:
          x5 = './/p[contains(@class, "event-type")]'
          p5 = el.xpath(x5)[0] # get property
          p5 = ' '.join(p5.text_content().split())     # clean & format it
          item[k5] = f'{p5}'
     except:
          item[k5] = ''
          pass

     k1 = 'Name of the Event'
     try:
          x1 = './/h4[contains(@class, "event-container")]'
          p1 = el.xpath(x1)[0]
          p1 = ' '.join(p1.text_content().split())
          item[k1] = f'{p1}'
     except:
          item[k1] = ''
          pass
     
     k2 = 'Sport'
     try:
          x2 = './/p[.//img[contains(@class, "sport-icon")]] '
          p2 = el.xpath(x2)[0]
          p2 = ' '.join(p2.text_content().split())
          item[k2] = f'{p2}'
     except:
          item[k2] = ''
          pass
     
     k3 = 'Date'
     try:
          x3 = './/p[.//i[contains(@class, "fa-calendar-alt")]]'
          p3 = el.xpath(x3)[0]
          p3 = ' '.join(p3.text_content().split())
          item[k3] = f'{p3}'
     except:
          item[k3] = ''
          pass
     
     k4 = 'Location'
     try:
          x4 = './/p[.//i[contains(@class, "fa-map-marker-alt")]]'
          p4 = el.xpath(x4)[0]
          p4 = ' '.join(p4.text_content().split())     
          item[k4] = f'{p4}'
     except:
          item[k4] = ''
          pass

     if len(item)!=0: # avoid empty items
          return item
     else:
          return ''
