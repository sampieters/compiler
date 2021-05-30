.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -36
        sw      $fp, 32($sp)
        sw      $ra, 28($sp)
        sw      $4, 24($sp)
        move    $fp, $sp
        li      $9, 10
        li      $10, 10
        sw      $10, 12($fp)
        li      $11, 20
        li      $12, 20
        sw      $12, 16($fp)
        li      $13, 30
        li      $14, 30
        sw      $14, 20($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        li      $v0, 0
        move    $sp, $fp
        lw      $4, 24($sp)
        lw      $ra, 28($sp)
        lw      $fp, 32($sp)
        addiu   $sp, $sp, 36
        li      $v0, 10
        syscall 