__AUTHOR__ = 'Reverier Xu'

from urllib import parse

properties = {
    'name': 'Escape',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码']
    }
}
defaults = {
    '开关': '编码'
}


def main(inp, settings):
    inputs = inp[0]

    if settings['开关'] == '编码':
        out = {0: parse.quote(inputs.encode(
            'unicode-escape')).replace('%5Cu', '%u')}
    else:
        out = {0: parse.unquote(
            inputs.replace('%u', '\\u').encode().decode('unicode-escape'))}
    return out
