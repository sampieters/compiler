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
        addiu   $sp, $sp, -32
        sw      $fp, 24($sp)
        sw      $ra, 20($sp)
        sw      $4, 16($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 0($fp)
        addiu   $8, $fp, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        li      $9, 10
        sw      $9, 0($8)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        lw      $9, 4($fp)
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        lw      $10, 4($fp)
        lw      $11, 4($fp)
        lw      $11, 0($11)
        addi    $11, $11, 1
        sw      $11, 12($fp)
        lw      $11, 12($fp)
        sw      $11, 0($10)
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        lw      $11, 4($fp)
        la      $4, string4_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string4_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 16($sp)
        lw      $ra, 20($sp)
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 