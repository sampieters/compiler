.data
double1: .double 5.000000e-01
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 24($sp)
        sw      $ra, 20($sp)
        sw      $4, 16($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        l.d     $f4, double1
        s.d     $f4, 4($fp)
        li      $8, 99
        sb      $8, 12($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        l.d     $f12, 4($fp)
        li      $2, 3
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        lb      $4, 12($fp)
        li      $2, 11
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 16($sp)
        lw      $ra, 20($sp)
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 