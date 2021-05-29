.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "\0A\00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 20($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        addiu   $9, $fp, 4
        sw      $$9, 12($fp)
        lw      $10, 3($fp)
        lw      $11, 0($$11)
        li      $12, 10
        sw      $12, 16($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $13, 3($fp)
        lw      $14, 0($$14)
        la      $4, string2_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $24, 3($fp)
        lw      $Error, 0($$Error)
        addiu   $Error, $Error, 1
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $Error, 3($fp)
        lw      $Error, 0($$Error)
        la      $4, string4_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 