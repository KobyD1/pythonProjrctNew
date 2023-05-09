# how to compare inages

from PIL import Image, ImageChops
im1 = Image.open("../Images/Ref/Google/Logo.png")
im2 = Image.open("../Images/Ref/Google/Error2.png")
assert im1.size  == im2.size, 'Images under test are not size equals '
translucent = Image.new("RGBA", im1.size, (255, 0, 0, 127))
mask = ImageChops.difference(im1, im2).convert("L")
im2.paste(translucent, (0, 0), mask)
im2.save("out.png")
