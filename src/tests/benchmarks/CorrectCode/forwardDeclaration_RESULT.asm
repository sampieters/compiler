.data
string1_1: .asciiz "Hello \00"
string2_1: .asciiz "World\n\00"
string3_1: .asciiz "World\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
$FUNC_f:
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        jr      $ra
                
g:      
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        sw      $ra, 12($sp)
        sw      $4, 8($sp)
        move    $fp, $sp
        la      $4, string2_1
        li      $2, 4
        syscall 
        jal     f
        sw      $2, 4($fp)
        la      $4, string3_1
        li      $2, 4
        syscall 
$FUNC_g:
        move    $sp, $fp
        lw      $4, 8($sp)
        lw      $ra, 12($sp)
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        jr      $ra
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        jal     f
        sw      $2, 12($fp)
        jal     g
        sw      $2, 16($fp)
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