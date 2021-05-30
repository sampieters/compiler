.data
string1_1: .asciiz ""
string1_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 28($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 0($fp)
        lw      $8, 0($fp)
        addiu   $8, $fp, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        lw      $8, 0($8)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        sw      $8, 20($fp)
        lw      $4, 20($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 28
        li      $v0, 10
        syscall 