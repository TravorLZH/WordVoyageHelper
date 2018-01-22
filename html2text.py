import re


def html2text(html):
    rmjs = re.compile("<script[^>]*>[^<]*</script>")
    rmcss = re.compile("<style[^>]*>[^<]*</style>")
    rmhtml = re.compile("<[^>]*>")
    text = re.sub(rmjs, "", html)
    text = re.sub(rmcss, "", text)
    text = re.sub(rmhtml, "", text)
    return text