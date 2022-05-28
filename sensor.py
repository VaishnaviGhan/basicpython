with open("sensor.txt","r") as f:
   content = f.read()
content=content.replace("pagal","ggggggg")
with open("sensor.txt","w") as f:
   f.write(content)