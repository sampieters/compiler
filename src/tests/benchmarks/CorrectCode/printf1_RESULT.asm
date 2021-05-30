.data
string1_1: .asciiz "Hello World!\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        li      $v0, 0
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $v0, 10
        syscall 