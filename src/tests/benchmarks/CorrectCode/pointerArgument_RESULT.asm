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
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        sw      $4, 8($fp)
        lw      $8, 8($fp)
        lw      $9, 8($fp)
        lw      $9, 0($9)
        addi    $9, $9, 1
        sw      $9, 16($fp)
        lw      $9, 16($fp)
        sw      $9, 0($8)
$FUNC_f:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        jr      $ra
                
main:   
        addiu   $sp, $sp, -60
        sw      $fp, 56($sp)
        sw      $ra, 52($sp)
        sw      $4, 48($sp)
        move    $fp, $sp
        li      $9, 0
        sw      $9, 24($fp)
        addiu   $9, $fp, 24
        sw      $9, 28($fp)
        lw      $9, 28($fp)
        li      $10, 42
        sw      $10, 0($9)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 24($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        lw      $10, 28($fp)
        lw      $10, 0($10)
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        lw      $11, 28($fp)
        lw      $12, 28($fp)
        lw      $12, 0($12)
        addi    $12, $12, 1
        sw      $12, 36($fp)
        lw      $12, 36($fp)
        sw      $12, 0($11)
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 24($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        lw      $12, 28($fp)
        lw      $12, 0($12)
        la      $4, string4_1
        li      $2, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string4_2
        li      $2, 4
        syscall 
        lw      $4, 24($fp)
        jal     f
        sw      $2, 40($fp)
        la      $4, string5_1
        li      $2, 4
        syscall 
        lw      $4, 24($fp)
        li      $2, 1
        syscall 
        la      $4, string5_2
        li      $2, 4
        syscall 
        lw      $14, 28($fp)
        lw      $14, 0($14)
        la      $4, string6_1
        li      $2, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string6_2
        li      $2, 4
        syscall 
        lw      $4, 28($fp)
        jal     f
        sw      $2, 44($fp)
        la      $4, string7_1
        li      $2, 4
        syscall 
        lw      $4, 24($fp)
        li      $2, 1
        syscall 
        la      $4, string7_2
        li      $2, 4
        syscall 
        lw      $15, 28($fp)
        lw      $15, 0($15)
        la      $4, string8_1
        li      $2, 4
        syscall 
        lw      $4, 28($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string8_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 48($sp)
        lw      $ra, 52($sp)
        lw      $fp, 56($sp)
        addiu   $sp, $sp, 60
        li      $2, 10
        syscall 