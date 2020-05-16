f =open("guido_bio.txt")
text=f.read()
f.close()

try:
    with open("guido_bio.txt") as fobj:
        bio=fobj.read()
except FileNotFoundError:
    bio=None

print(bio)


oceans=["Pacific","ATlantic","Indian","Southern","Arctic"]

with open("oceans.txt","w") as f:
    for ocean in oceans:
        print(ocean, "1", file=f )


with open("oceans.txt") as f:
    print(f.read())