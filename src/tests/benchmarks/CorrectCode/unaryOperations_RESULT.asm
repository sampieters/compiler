.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "; \00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "; \00"
string5_1: .asciiz ""
string5_2: .asciiz "; \00"
string6_1: .asciiz ""
string6_2: .asciiz "; \00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -60
        sw      $fp, 56($sp)
        sw      $ra, 52($sp)
        sw      $4, 48($sp)
        move    $fp, $sp
        li      $8, 9
        sw      $8, 0($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        li      $4, 9
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $8, 0($fp)
        addiu   $8, $8, 1
        sw      $8, 0($fp)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        li      $9, 15
        li      $10, 15
        sw      $10, 12($fp)
        li      $11, 12
        li      $12, 12
        sw      $12, 16($fp)
        li      $12, 12
        li      $13, 12
        sw      $13, 20($fp)
        lw      $15, 8($fp)
        subi    $15, $15, 1
        sw      $15, 24($fp)
        lw      $15, 24($fp)
        sw      $15, 28($fp)
        lw      $15, 28($fp)
        sw      $15, 32($fp)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        la      $4, string4_1
        li      $v0, 4
        syscall 
        lw      $4, 20($fp)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        lw      $24, 20($fp)
        addiu   $24, $24, 1
        sw      $24, 20($fp)
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 20($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $None, 4($fp)
        subi    $None, $None, 1
        sw      $None, 36($fp)
        lw      $None, 36($fp)
        sw      $None, 40($fp)
        lw      $None, 40($fp)
        sw      $None, 44($fp)
        la      $4, string6_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $4, 48($sp)
        lw      $ra, 52($sp)
        lw      $fp, 56($sp)
        addiu   $sp, $sp, 60
        li      $v0, 10
        syscall 