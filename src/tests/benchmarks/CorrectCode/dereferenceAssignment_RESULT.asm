.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "\n\00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -36
        sw      $fp, 36($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        addiu   $8, $fp, 4
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        sw      $8, 20($fp)
        lw      $8, 20($fp)
        li      $9, 10
        sw      $9, 0($8)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $9, 20($fp)
        lw      $9, 0($9)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $9, 24($fp)
        lw      $4, 24($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $9, 20($fp)
        lw      $10, 20($fp)
        lw      $10, 0($10)
        addi    $10, $10, 1
        sw      $10, 28($fp)
        lw      $10, 28($fp)
        sw      $10, 0($9)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $10, 20($fp)
        lw      $10, 0($10)
        la      $4, string4_1
        li      $v0, 4
        syscall 
        sw      $10, 32($fp)
        lw      $4, 32($fp)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 36($sp)
        addiu   $sp, $sp, 40
        li      $v0, 10
        syscall 