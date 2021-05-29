.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 24($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        addiu   $9, $fp, 4
        sw      $$9, 12($fp)
        lw      $10, 3($fp)
        addiu   $11, $fp, 3
        sw      $$11, 20($fp)
        lw      $12, 3($fp)
        lw      $13, 0($$13)
        lw      $14, 4($fp)
        lw      $24, 0($$24)
        lw      $Error, 0($$Error)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 28
        li      $v0, 10
        syscall 