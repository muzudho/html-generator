#
# Note.
#
# Root directory: Visual studio code workspace root.
#
file_name = "./html-generator/auto-generated/view.html"

try:
    file = open(file_name, 'w', encoding='utf-8')
    file.write(
        """
<html>
<head>
    <title>サンプル</title>
</head>
<body>
</body>
</html>
"""
    )
except Exception as e:
    print(e)
finally:
    file.close()
