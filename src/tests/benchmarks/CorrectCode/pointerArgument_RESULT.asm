.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "\n\00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "\n\00"
string5_1: .asciiz ""
string5_2: .asciiz "; \00"
string6_1: .asciiz ""
string6_2: .asciiz "\n\00"
string7_1: .asciiz ""
string7_2: .asciiz "; \00"
string8_1: .asciiz ""
string8_2: .asciiz "\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -24
        sw      $fp, 20($sp)
        move    $fp, $sp
        sw      $4, 8($fp)
        lw      $8, 8($fp)
        lw      $9, 8($fp)
        lw      $9, 0($9)
        addi    $9, $9, 1
        sw      $9, 16($fp)
        lw      $9, 16($fp)
        sw      $9, 0($8)
        move    $sp, $fp
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        jr      $ra
                
main:   
        addiu   $sp, $sp, -44
        sw      $fp, 40($sp)
        move    $fp, $sp
        li      $9, 0
        sw      $9, 24($fp)
        addiu   $9, $fp, 24
        sw      $9, 28($fp)
        lw      $9, 28($fp)
        li      $10, 42
        sw      $10, 0($9)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $10, 28($fp)
        lw      $10, 0($10)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $11, 28($fp)
        lw      $12, 28($fp)
        lw      $12, 0($12)
        addi    $12, $12, 1
        sw      $12, 36($fp)
        lw      $12, 36($fp)
        sw      $12, 0($11)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $12, 28($fp)
        lw      $12, 0($12)
        la      $4, string4_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        jal     f
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $14, 28($fp)
        lw      $14, 0($14)
        la      $4, string6_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        jal     f
        la      $4, string7_1
        li      $v0, 4
        syscall 
        lw      $4, 24($fp)
        li      $v0, 1
        syscall 
        la      $4, string7_2
        li      $v0, 4
        syscall 
        lw      $15, 28($fp)
        lw      $15, 0($15)
        la      $4, string8_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $v0, 1
        syscall 
        la      $4, string8_2
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 40($sp)
        addiu   $sp, $sp, 44
        li      $v0, 10
        syscall 