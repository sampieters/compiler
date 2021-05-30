.data
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        li      $8, 10
        sw      $8, 0($fp)
        addiu   $8, $fp, 0
        sw      $8, 4($fp)
        addiu   $8, $fp, 4
        sw      $8, 12($fp)
        lw      $8, 4($fp)
        lw      $8, 0($8)
        lw      $9, 12($fp)
        lw      $9, 0($9)
        lw      $10, 0($10)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        lw      $4, 12($fp)
        lw      $4, 0($4)
        lw      $4, 0($4)
        li      $2, 1
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 