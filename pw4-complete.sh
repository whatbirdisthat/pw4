#!/usr/bin/env bash


_pw4_complete()
{
    local cur_word prev_word type_list

    # COMP_WORDS is an array of words in the current command line.
    # COMP_CWORD is the index of the current word (the one the cursor is
    # in). So COMP_WORDS[COMP_CWORD] is the current word; we also record
    # the previous word here, although this specific script doesn't
    # use it yet.
    cur_word="${COMP_WORDS[COMP_CWORD]}"
    prev_word="${COMP_WORDS[COMP_CWORD-1]}"

    # Ask pss to generate a list of types it supports
    type_list=`cat ~/.gnupg/pw4-all.txt`

        # COMPREPLY is the array of possible completions, generated with
        # the compgen builtin.
        COMPREPLY=( $(compgen -W "${type_list}" -- ${cur_word}) )
    return 0
}

# Register _pw4_complete to provide completion for the following commands
complete -F _pw4_complete pw4