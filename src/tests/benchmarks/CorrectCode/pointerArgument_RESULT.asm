.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "\0A\00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "\0A\00"
string5_1: .asciiz ""
string5_2: .asciiz "; \00"
string6_1: .asciiz ""
string6_2: .asciiz "\0A\00"
string7_1: .asciiz ""
string7_2: .asciiz "; \00"
string8_1: .asciiz ""
string8_2: .asciiz "\0A\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        lw      $8, 2($fp)
        lw      $9, 0($$9)
        addiu   $10, $10, 1
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        jr      $ra
                
main:   
        addiu   $sp, $sp, -28
        sw      $fp, 28($sp)
        move    $fp, $sp
        li      $11, 0
        sw      $11, 12($fp)
        lw      $11, 12($fp)
        addiu   $12, $fp, 12
        sw      $$12, 20($fp)
        lw      $13, 3($fp)
        lw      $14, 0($$14)
        li      $24, 42
        sw      $24, 24($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $Error, 3($fp)
        lw      $Error, 0($$Error)
        la      $4, string2_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        lw      $Error, 3($fp)
        lw      $Error, 0($$Error)
        addiu   $Error, $Error, 1
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
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
        lw      $Error, 12($fp)
        addiu   $Error, $fp, 12
                
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
        lw      $Error, 3($fp)
        lw      $Error, 0($$Error)
        la      $4, string6_1
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string6_2
        li      $v0, 4
        syscall 
        lw      $4, 3($fp)
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
        lw      $Error, 3($fp)
        lw      $Error, 0($$Error)
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
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $v0, 10
        syscall 