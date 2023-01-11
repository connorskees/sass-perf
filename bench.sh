bench() {
    hyperfine "./dart-sass/sass $1 $2" "grass $1 $2" "./sassc/bin/sassc $1 $2" --warmup 5
}

# bench bootstrap/scss/bootstrap.scss
# bench bulma/bulma.sass
# bench small-plain.scss
# bench large-plain.scss
# bench preceding-sparse-extend.scss
# bench following-sparse-extend.scss
# bench preceding-dense-extend.scss
# bench following-dense-extend.scss
# bench single-bootstrap.scss
# bench large-bootstrap.scss
# bench a11ycolor.scss
# bench duomo.scss
bench carbon.scss -Iibm-cloud-cognitive/node_modules
