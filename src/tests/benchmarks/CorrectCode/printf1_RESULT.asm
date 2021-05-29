.data
string1_1: .asciiz "Hello World!\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        li      $v0, 10
        syscall 