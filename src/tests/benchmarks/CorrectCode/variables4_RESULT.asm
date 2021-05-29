.data
string1_1: .asciiz ""
string1_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 4($fp)
        lw      $9, 0($fp)
        addiu   $10, $fp, 0
        sw      $$10, 12($fp)
        lw      $11, 4($fp)
        lw      $12, 0($$12)
        la      $4, string1_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 