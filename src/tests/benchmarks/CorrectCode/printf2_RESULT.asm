.data
string1_1: .asciiz ""
string1_2: .asciiz " "
string1_3: .asciiz "!\0A\00"
string2_1: .asciiz "Hello\00"
string3_1: .asciiz "World\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        la      $4, string2
        li      $v0, 4
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        la      $4, string3
        li      $v0, 4
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        li      $v0, 10
        syscall 