.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -44
        sw      $fp, 48($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 0($fp)
        addiu   $8, $fp, 0
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        sw      $8, 12($fp)
        addiu   $8, $fp, 12
        sw      $8, 20($fp)
        lw      $8, 20($fp)
        sw      $8, 28($fp)
        lw      $8, 12($fp)
        lw      $8, 0($8)
        lw      $9, 28($fp)
        lw      $9, 0($9)
        lw      $10, 0($10)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        sw      $8, 36($fp)
        lw      $4, 36($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        sw      $10, 40($fp)
        lw      $4, 40($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 48($sp)
        addiu   $sp, $sp, 48
        li      $v0, 10
        syscall 