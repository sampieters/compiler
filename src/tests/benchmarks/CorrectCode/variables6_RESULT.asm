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
        lw      $9, 0($fp)
        addiu   $10, $fp, 0
        sw      $$10, 12($fp)
        lw      $11, 4($fp)
        addiu   $12, $fp, 4
        sw      $$12, 20($fp)
        lw      $13, 4($fp)
        lw      $14, 0($$14)
        lw      $24, 12($fp)
        lw      $Error, 0($$Error)
        lw      $Error, 0($$Error)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
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