.data
string1: .asciiz "%s %s!\0A\00"
string2: .asciiz "Hello\00"
string3: .asciiz "World\00"
.globl main
.text
                
main:   
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $6,string1
        la      $6,string2
        la      $6,string3
        la      $6,string2
        li      $v0,4
        syscall 
        la      $6,string3
        li      $v0,4
        syscall 
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        li      $v0,10
        syscall 