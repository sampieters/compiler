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
        addiu   $sp, $sp, -20
        sw      $fp, 20($sp)
        move    $fp, $sp
        sw      $4, 16($fp)
        lw      $8, 16($fp)
        lw      $8, 0($8)
        addiu   $9, $8, 1
        sw      $8, 3($fp)
        nop     
        move    $sp, $fp
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        jr      $ra
                
main:   
        addiu   $sp, $sp, -72
        sw      $fp, 72($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 28($fp)
        lw      $8, 28($fp)
        addiu   $8, $fp, 28
        sw      $8, 36($fp)
        lw      $8, 36($fp)
        sw      $8, 44($fp)
        lw      $8, 44($fp)
        li      $9, 42
        sw      $9, 0($8)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $9, 44($fp)
        lw      $9, 0($9)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $9, 48($fp)
        lw      $4, 48($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $9, 44($fp)
        lw      $9, 0($9)
        addiu   $10, $9, 1
        sw      $9, 10($fp)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $9, 44($fp)
        lw      $9, 0($9)
        la      $4, string4_1
        li      $v0, 4
        syscall 
        sw      $9, 52($fp)
        lw      $4, 52($fp)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        lw      $9, 28($fp)
        addiu   $9, $fp, 28
        sw      $9, 60($fp)
        lw      $4, 60($fp)
        jal     f
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $9, 44($fp)
        lw      $9, 0($9)
        la      $4, string6_1
        li      $v0, 4
        syscall 
        sw      $9, 64($fp)
        lw      $4, 64($fp)
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        lw      $4, 44($fp)
        jal     f
        la      $4, string7_1
        li      $v0, 4
        syscall 
        lw      $4, 28($fp)
        li      $v0, 1
        syscall 
        la      $4, string7_2
        li      $v0, 4
        syscall 
        lw      $9, 44($fp)
        lw      $9, 0($9)
        la      $4, string8_1
        li      $v0, 4
        syscall 
        sw      $9, 68($fp)
        lw      $4, 68($fp)
        li      $v0, 1
        syscall 
        la      $4, string8_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 72($sp)
        addiu   $sp, $sp, 76
        li      $v0, 10
        syscall 