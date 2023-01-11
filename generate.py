"""
Generate sample Sass files
"""

# def create(name: str, contents: str)

with open("small-plain.scss", "w") as f:
    f.write(".foo {a: b}" * 4)

with open("large-plain.scss", "w") as f:
    f.write(".foo {a: b}" * (2 ** 17))

with open("preceding-sparse-extend.scss", "w") as f:
    f.write(".x {@extend .y}")
    f.write(".foo {a: b}" * (2 ** 17))
    f.write(".y {a: b}")

with open("following-sparse-extend.scss", "w") as f:
    f.write(".y {a: b}")
    f.write(".foo {a: b}" * (2 ** 17))
    f.write(".x {@extend .y}")

with open("preceding-dense-extend.scss", "w") as f:
    f.write(".bar {@extend .foo}")
    f.write(".foo {a: b}" * (2 ** 17))

with open("following-dense-extend.scss", "w") as f:
    f.write(".foo {a: b}" * (2 ** 17))
    f.write(".bar {@extend .foo}")

with open("single-bootstrap.scss", "w") as f:
    f.write("@import 'bootstrap/scss/bootstrap';")

with open("large-bootstrap.scss", "w") as f:
    f.write("@import 'bootstrap/scss/bootstrap';" * 16)

with open("a11ycolor.scss", "w") as f:
    f.write("""
        @import 'sass-a11ycolor/dist';
        

        x {
            // Adapted from a11ycolor's test1.scss, which at one point was much slower
            // in JS than in the Dart VM.
            y: AU-a11ycolor(red, blue)
                AU-a11ycolor(#646464, #E0E0E0)
                AU-a11ycolor(green, blue)
                AU-a11ycolor(pink, blue)
                AU-a11ycolor(blue, blue)
                AU-a11ycolor(#c0c0c0, #c0c0c0)
                AU-a11ycolor(#231284, #ccc)
                AU-a11ycolor(#fff, #fff);
        }
    """)

with open("duomo.scss", "w") as f:
    f.write("@import 'duomo/scripts/duomo.scss';")

with open("carbon.scss", "w") as f:
    f.write("@import 'ibm-cloud-cognitive/packages/cloud-cognitive/src/index-without-carbon-released-only';")
