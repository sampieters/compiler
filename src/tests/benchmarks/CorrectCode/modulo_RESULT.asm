.data
string1_1: .asciiz ""
string1_2: .asciiz "\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 12($sp)
        sw      $ra, 8($sp)
        sw      $4, 4($sp)
        move    $fp, $sp
        li      $8, 1
        sw      $8, 0($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 4($sp)
        lw      $ra, 8($sp)
        lw      $fp, 12($sp)
        addiu   $sp, $sp, 16
        li      $2, 10
        syscall 