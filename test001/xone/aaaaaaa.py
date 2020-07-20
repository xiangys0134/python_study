import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='myapp1.log',
                    filemode='a+')

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# console.setFormatter(formatter)
#
# logging.getLogger('').addHandler(console)


# logging.info('Jackdaws love my big sphinx of quartz.')



logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')


import os

ab_path = os.path.abspath('./')
# print(ab_path)

res = os.path.join(ab_path,'aaa.log')

print(res)


res = ab_path = os.path.abspath('/root/data/ext')
print(res)