# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard :test do
  watch /^facebook\/(.+)\.py$/ do |m|
    `nosetests --with-color tests/test_#{m[1]}.py`
  end
end
