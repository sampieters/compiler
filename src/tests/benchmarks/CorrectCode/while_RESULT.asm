.data
string1_1: .asciiz ""
string1_2: .asciiz ";\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        sw      $ra, 12($sp)
        sw      $4, 8($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 0($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $8, 0($fp)
        slti    $8, $8, 5
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        beq     $8, $0, $L1
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $8, 0($fp)
        addiu   $8, $8, 1
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
        j       $L0
        # END WHILE BODY
                
$L1:    
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 8($sp)
        lw      $ra, 12($sp)
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $2, 10
        syscall 