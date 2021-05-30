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
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        lw      $8, 2($fp)
        lw      $8, 0($8)
        addiu   $9, $9, 1
        sw      $8, 3($fp)
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        jr      $ra
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 24($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        addiu   $8, $fp, 12
                
        sw      $8, 20($fp)
        lw      $8, 20($fp)
        lw      $8, 0($8)
        li      $9, 42
        sw      $9, 4($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
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
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $10, 20($fp)
        lw      $10, 0($10)
        addiu   $11, $11, 1
        sw      $10, 10($fp)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
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
                
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        lw      $11, 12($fp)
        addiu   $11, $fp, 12
                
        jal     f
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $11, 20($fp)
        lw      $11, 0($11)
        la      $4, string6_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        lw      $4, 20($fp)
        jal     f
        la      $4, string7_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string7_2
        li      $v0, 4
        syscall 
        lw      $12, 20($fp)
        lw      $12, 0($12)
        la      $4, string8_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string8_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 28
        li      $v0, 10
        syscall 