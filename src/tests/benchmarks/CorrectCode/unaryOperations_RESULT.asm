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
        addiu   $sp, $sp, -20
        sw      $fp, 20($sp)
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
        addiu   $9, $9, 1
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $10, 3($fp)
        li      $12, 15
        sw      $12, 8($fp)
        lw      $13, 3($fp)
        li      $24, 12
        sw      $24, 12($fp)
        li      $Error, 12
        sw      $Error, 16($fp)
        lw      $Error, 3($fp)
        addiu   $Error, $Error, -1
        lw      $Error, 3($fp)
        la      $4, string3_1
        li      $v0, 4
        syscall 
                
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
        lw      $Error, 4($fp)
        addiu   $Error, $Error, 1
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $Error, 3($fp)
        addiu   $Error, $Error, -1
        lw      $Error, 3($fp)
        la      $4, string6_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 