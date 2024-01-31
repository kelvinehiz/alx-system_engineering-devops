In this project, We take a look at  how to use regular expressions. We then went ahead to  build
them using Ruby's Oniguruma library.

All code in this directory was tested using [Rubular](https://rubular.com/). Rubular is a Ruby-based regular expression editor. It's a handy way to test regular expressions as you write them.


_Note: Each Ruby script in the project matches regular expressions based on an
argument passed to it via the command line._

  * [0-simply_match_school.rb](./0-simply_match_school.rb): Ruby script that
  matches the regular expression `School`.

  * [1-repetition_token_0.rb](./1-repetition_token_0.rb): Ruby script that matches
  the regular expression `hbn` with between 2-5 `t`'s in between `hb` and `n`.

  * [2-repetition_token_1.rb](./2-repetition_token_1.rb): Ruby script that matches
  the regular expression `hn` with 0 or 1 occurrences of `b` and 0 or 1
  occurrences of `t` in between `h` and `n`.

  * [3-repetition_token_2.rb](./3-repetition_token_2.rb): Ruby script that matches
  the regular expression `hbn` with 1 or more `t`'s in between `hb` and `n`.

  * [4-repetition_token_3.rb](./4-repetition_token_3.rb): Ruby script that matches the
  regular expression `hbn` with 0 or more `t`'s in between `hb` and `n`.

  * [5-beginning_and_end.rb](./5-beginning_and_end.rb): Ruby script that matches a
  regular expression starting with `h` and ending with `n` with any single character in between.

  * [6-phone_number.rb](./6-phone_number.rb): Ruby script that matches a regular expression
  representing a 10-digit phone number.

  * [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb): Ruby script that
  matches regular expressions of uppercase letters.

  * [100-textme.rb](./100-textme.rb): Ruby script that runs statistics on TextMe app text
  message transcations.
  * Output: `[SENDER],[RECEIVER],[FLAGS]` where
    * `[SENDER]` is the sender phone number or name (including country code
    if present).
    * `[RECEIVER]` is the receiver phone number or name (including country code
    if present).
    * `[FLAGS]` is the flags that were used.
