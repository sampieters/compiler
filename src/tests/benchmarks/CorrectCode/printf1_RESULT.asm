.data
string1_1: .asciiz "Hello World!\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -4
        sw      $fp, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 0($sp)
        addiu   $sp, $sp, 4
        li      $v0, 10
        syscall 