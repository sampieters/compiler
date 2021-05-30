.data
float1: .float 5.000000e-01
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -36
        sw      $fp, 32($sp)
        sw      $ra, 28($sp)
        sw      $4, 24($sp)
        move    $fp, $sp
        li      $8, 5
        li      $9, 5
        sw      $9, 4($fp)
        l.s     $f4, float1
        l.s     $f5, float1
        s.s     $f5, 12($fp)
        li      $9, 99
        li      $10, 99
        sb      $10, 20($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        l.s     $f12, 12($fp)
        li      $2, 2
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        lb      $4, 20($fp)
        li      $2, 11
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 24($sp)
        lw      $ra, 28($sp)
        lw      $fp, 32($sp)
        addiu   $sp, $sp, 36
        li      $2, 10
        syscall 