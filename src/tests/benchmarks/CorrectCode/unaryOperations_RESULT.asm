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
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        li      $8, 9
        sw      $8, 4($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        li      $4, 9
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $8, 4($fp)
        addiu   $8, $8, 1
        sw      $8, 4($fp)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $8, 3($fp)
        li      $9, 15
        sw      $9, 3($fp)
        lw      $9, 3($fp)
        li      $10, 12
        sw      $10, 34($fp)
        li      $10, 12
        sw      $10, 4($fp)
        lw      $10, 3($fp)
        addiu   $11, $11, -1
        sw      $10, 34($fp)
        lw      $10, 3($fp)
        la      $4, string3_1
        li      $v0, 4
        syscall 
        sw      $10, 8($fp)
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        la      $4, string4_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        lw      $10, 4($fp)
        addiu   $10, $10, 1
        sw      $10, 4($fp)
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $10, 3($fp)
        addiu   $11, $11, -1
        sw      $10, 3($fp)
        lw      $10, 3($fp)
        la      $4, string6_1
        li      $v0, 4
        syscall 
        sw      $10, 12($fp)
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 